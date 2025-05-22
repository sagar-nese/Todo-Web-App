import streamlit as st
import TodoFunctions

Existing_Todos = TodoFunctions.file_read()

def add_todo():
    mytodo = st.session_state["new_todo"] + '\n'
    Existing_Todos.append(mytodo)
    TodoFunctions.file_write(Existing_Todos)


st.title("My Todo App")
st.subheader("Here is your Todo List")
st.write("This App helps to plan your days, weeks and months Activities")

st.text_input(label="Hey! There, Have you planned your days?", placeholder="Add new todo...", on_change=add_todo, key='new_todo')

for index, todo in enumerate(Existing_Todos):
    value = st.checkbox(todo, key=todo)
    if value:
        Existing_Todos.pop(index)
        TodoFunctions.file_write(Existing_Todos)
        del st.session_state[todo]
        st.rerun()
