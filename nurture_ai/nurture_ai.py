# nurture_ai.py
import reflex as rx
from nurture_ai.pages import dashboard
import nurture_ai.state as state_module

@rx.page(route="/", title="Nurture")
def index():
    return rx.fragment(
        rx.form_control(
            rx.form_label("Name", html_for="name"),
            rx.input(
                placeholder="Enter your name",
                on_change=state_module.FormState.set_name,
            ),
        ),
        rx.form_control(
            rx.form_label("Phone Number", html_for="phone"),
            rx.input(
                type="tel",
                placeholder="Enter your phone number",
                on_change=state_module.FormState.set_phone,
            ),
        ),
        rx.button(
            "Start",
            on_click=rx.redirect("/dashboard"),   # Use rx.redirect to dashboard
        ),
    )

app = rx.App()
app.add_page(index)
app.add_page(dashboard)
app.compile()