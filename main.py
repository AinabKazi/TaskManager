import streamlit as st

# Sample data (tasks stored in a list)
tasks = []

def add_task(title):
    new_task = {"id": len(tasks) + 1, "title": title, "completed": False}
    tasks.append(new_task)

def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]

def main():
    st.title("Task Tracker")

    # Add Task
    new_task = st.text_input("New Task:")
    if st.button("Add Task") and new_task:
        add_task(new_task)

    # Display Tasks
    st.subheader("Tasks")
    for task in tasks:
        task_status = "Completed" if task["completed"] else "Not Completed"
        col1, col2, col3 = st.columns([1, 3, 1])
        with col1:
            st.checkbox("", value=task["completed"], key=str(task["id"]))
        with col2:
            st.write(f"{task['title']} - {task_status}")
        with col3:
            if st.button("Complete", key=f"complete_{task['id']}"):
                complete_task(task["id"])
            if st.button("Delete", key=f"delete_{task['id']}"):
                delete_task(task["id"])

if __name__ == "__main__":
    main()
