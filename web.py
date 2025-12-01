import streamlit as st
import functions as f

todos = f.get_todos()

def add_todo():
    todo =st.session_state["new_todo"]
    todos.append(todo + "\n")
    st.session_state.new_todo = ""
    f.write_todos(todos)

def clear_all_completed():
    global todos

    new_todos = []
    for todo in todos:
        checkbox_key = todo + "_key"
        if not st.session_state.get(checkbox_key, False):
            new_todos.append(todo)

        todos = new_todos
        f.write_todos(todos)
        for todo in todos:
            st.session_state.pop(todo.strip() + "_key", None)

st.title("My Todo App")
st.subheader("Task management application")
st.write("This app is meant to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo + "_key")

st.text_input("New todo",
                key="new_todo",
                placeholder="Enter a new todo...",
                label_visibility="collapsed",
                on_change=add_todo)

st.button("Clear All Completed", key="clear_all_completed", on_click=clear_all_completed)

