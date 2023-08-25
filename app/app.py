# Import reflex, style and state
import reflex as rx
from app import style
from app.state import State

def qa(question:str, answer:str) -> rx.Component: 
    return rx.box(
        rx.box(rx.text(question, style=style.question_style), text_align="right"), 
        rx.box(rx.text(answer, style=style.answer_style), text_align="left"),
        margin_y="1em" 
    )
    

def chat() -> rx.Component: 
    return rx.box(
        rx.foreach(State.chat_history, lambda messages: qa(messages[0], messages[1]))
    )

def action_bar() -> rx.Component: 
    return rx.hstack(
        rx.input(placeholder="Ask a question", on_blur=State.set_question, style=style.input_style), 
        rx.button("Ask", on_click=State.answer, style=style.button_style),
    )

def navbar():
    return rx.box(
        rx.hstack(
            rx.image(src="download.ico"),
            rx.heading("watsonx.ai Chat"),
        ),
        rx.spacer(),
        width="100%",
        top="0px",
    )

def index() -> rx.Component:
    return rx.container(navbar(), chat(), action_bar())

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
