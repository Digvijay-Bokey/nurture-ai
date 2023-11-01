# dashboard.py
# from nurture_ai.humePG import init_session
import reflex as rx

from nurture_ai.state import FormState
# from nurture_ai.hume_state import HumeState


@rx.page(route='/dashboard', title='Dashboard')
def dashboard() -> rx.Component:
    """The dashboard page."""
    # init_session()
    
    return rx.vstack(
        rx.heading("Dashboard", font_size="3em"),
        rx.text(f"Welcome, {FormState.name}'s parent!"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/dashboard.py"),
        ),
    rx.button("Toggle", on_click=FormState.toggleRun),
    rx.cond(
        FormState.run,
        rx.text("Start", color="green"),
        rx.text("Stop", color="red"),
    ),
        on_mount=FormState.init_session
        # init_session()  # Adds the webcam session button to the dashboard
    )
