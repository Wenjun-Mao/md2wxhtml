"""
Default theme.
Clean and simple styling with blue accents.
"""

def get_css() -> str:
    """Get the default theme CSS."""
    return """
        .wechat-content {
            color: #333;
            background-color: #fff;
        }
        
        .wechat-content h1 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 5px;
        }
        
        .wechat-content h2 {
            color: #34495e;
            border-bottom: 1px solid #bdc3c7;
            padding-bottom: 3px;
        }
        
        .wechat-content h3 {
            color: #34495e;
        }
        
        .wechat-content blockquote {
            border-left-color: #3498db;
            background-color: #ecf0f1;
        }
        
        .wechat-content a {
            color: #3498db;
            border-bottom-color: #3498db;
        }
        
        .wechat-content strong {
            color: #2c3e50;
        }

        .wechat-content p.list-highlight {
            background: none;
            border-left: none;
            padding: 0;
            border-radius: 0;
            color: rgb(44, 62, 80);
            margin-bottom: 16px;
        }
        
        .wechat-content p.list-highlight span.list-highlight-span {
            background: rgba(52, 152, 219, 0.10);
            border-left: 4px solid rgb(52, 152, 219);
            padding: 6px 12px;
            border-radius: 6px;
            color: rgb(44, 62, 80);
            margin-right: 6px;
        }
        """
