import streamlit as st
import function

todos_list = function.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos_list.append(todo)
    function.save_file(todos_list)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos_list):
    check_box = st.checkbox(todo,
                            key=todo)
    if check_box:
        todos_list.pop(index)
        function.save_file(todos_list)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add new todo",
              placeholder="Add new todo...",
              on_change=add_todo,
              key="new_todo")

