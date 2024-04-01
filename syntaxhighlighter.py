from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter

class PythonSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(QColor("#ADD8E6"))
        keywordFormat.setFontWeight(QFont.Bold)
        keywords = ["False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue",
                    "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import",
                    "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"]
        self.keywordPattern = QRegularExpression(r"\b(" + "|".join(keywords) + r")\b")
        
        quotationFormat = QTextCharFormat()
        quotationFormat.setForeground(QColor("#90EE90"))
        self.quotationPattern = QRegularExpression(r'\".*?\"|\'.*?\'')
        
        commentFormat = QTextCharFormat()
        commentFormat.setForeground(QColor("#D3D3D3"))
        self.commentPattern = QRegularExpression(r'#[^\n]*')
        
        self.rules = [
            (keywordFormat, self.keywordPattern),
            (quotationFormat, self.quotationPattern),
            (commentFormat, self.commentPattern)
        ]
    
    def highlightBlock(self, text):
        for format, pattern in self.rules:
            expression = pattern.globalMatch(text)
            while expression.hasNext():
                match = expression.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)
