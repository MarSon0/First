import flet as ft
from flet import Page
import asyncio
import pickle


import sqlite3
conn = sqlite3.connect("account.db")
cursor = conn.cursor()

async def main(page: Page) -> None:

    page.title = "Glam Lab Clicker"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor ="#141221"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {"FulboArgenta": "ofont.ru_Fulbo Argenta.ttf"}
    page.theme = ft.Theme(font_family="FulboArgenta")


    async def score_up(event: ft.ContainerTapEvent) -> None:
        score.data += 1
        score.value = str(score.data)

        image.scale = 0.95

        progress_bar.value += (1 / 100)

        if score.data % 10 == 0:

            with open("data.pkl", "rb") as f:
                user_id = pickle.load(f)

            cursor.execute("UPDATE `users` SET `record` = `record` + (?) WHERE `user_id` = (?)", (1, user_id))
            conn.commit()

            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value="+10",
                    size=20,
                    color="#bcc5c5",
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor="#25223a"
            )

            page.snack_bar.open = True
            progress_bar.value = 0

        await page.update_async()

        await asyncio.sleep(0.1)
        image.scale = 1

        await page.update_async()

    score = ft.Text(value="0", size=100, data=0)
    score_counter = ft.Text(
        size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN)
    )
    image = ft.Image(
        src="4.png",
        fit=ft.ImageFit.CONTAIN,
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)
    )
    progress_bar = ft.ProgressBar(
        value=0,
        width=page.width-100,
        bar_height=20,
        color='#1a2bea',
        bgcolor="#bcc5c5"
    )

    await page.add_async(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click=score_up,
            margin=ft.Margin(0, 0, 0, 15)
        ),
        ft.Container(
            content=progress_bar,
            border_radius=ft.BorderRadius(10, 10, 10, 10)
        )
    )

if __name__ == "__main__":
    ft.app(target=main, view=None, port=8000)

# ft.WEB_BROWSER