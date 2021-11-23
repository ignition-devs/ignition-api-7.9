from java.awt import Container


class JTextComponent(Container):
    _text = "Text"

    def getText(self):
        return self._text

    def setText(self, t):
        self._text = t
