import gasp

gasp.begin_graphics()
gasp.Circle((200, 200), 60)
gasp.Line((100, 400), (580, 200))
gasp.Box((400, 350), 120, 100)

gasp.update_when('key_pressed')
end_graphics()