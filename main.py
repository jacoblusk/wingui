import wingui

if __name__ == "__main__":
    msg_handler = wingui.MessageHandler()
    main_window = wingui.Window(msg_handler, "Main", (480, 600))

    def btn_onclick():
        child_window = wingui.Window(msg_handler, "Child", (256, 256), parent=main_window,
            onclose=lambda: main_window.set_enable(True)
        )

        edit_text = wingui.EditText(child_window, "", (10, 23), (100, 23))

        def submit_onclick():
            print(edit_text.get_text())
            child_window.close()

        wingui.Button(child_window, "Submit", (120, 23), (110, 23), onclick=submit_onclick)
        
        child_window.show()
        main_window.set_enable(False)

    wingui.Button(main_window, "Button", (50, 50), (80, 23), onclick=btn_onclick)
    wingui.Label(main_window, "Label", (50, 100), (50, 23))

    main_window.show()
    msg_handler.run()