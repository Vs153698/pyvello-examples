import pyvello as ui

def alert_button_clicked():
    print("Button clicked!")

with ui.App(title="Component Demo", theme="light", palette="red", enable_graph=False) as app:
    ui.title("Fix Duplicate Rendering in Left/Right Panel Demo", variant="h3", color="primary", class_name="mb-4")
    col1, col2 = ui.columns(2)
    with col1:
        ui.title("Left Panel")
        ui.text("Configure parameters here.")
    with col2:
        ui.title("Right Panel")
        ui.metric(label="System Health", value="99.98%", delta="+0.04%")

    ui.button("Click me", on_click=alert_button_clicked,confirm="Are you sure you want to click this button?")
    ui.callout("All subagent tools executed successfully.", variant="success")
    ui.badge("Production Ready", variant="default")

if __name__ == "__main__":
    app.launch(port=8080)