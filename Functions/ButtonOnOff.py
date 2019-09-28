class ButtonOnOff:
    def __init__(self, button_state):
        self.state = button_state
        self.state_switch()

    def state_switch(self):
        if self.state:
            self.state = False
            return True

        else:
            self.state = True
            return False
