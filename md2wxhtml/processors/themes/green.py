"""
Fresh and natural green color scheme.
Perfect for nature, health, and eco-friendly content.
"""

def get_css() -> str:
    """Get the Green theme CSS."""
    return """
        .wechat-content {
            background-color: #f8fff8;
            color: #2d4a2b;
        }
        
        .wechat-content h1 {
            color: #1e7d32;
            border-bottom: 2px solid #4caf50;
            padding-bottom: 5px;
        }
        
        .wechat-content h2 {
            color: #388e3c;
            border-bottom: 1px solid #66bb6a;
            padding-bottom: 3px;
        }
        
        .wechat-content h3 {
            color: #4caf50;
        }
        
        .wechat-content blockquote {
            border-left-color: #4caf50;
            background-color: #e8f5e8;
        }
        
        .wechat-content a {
            color: #2e7d32;
            border-bottom-color: #4caf50;
        }
        
        .wechat-content strong {
            color: #1b5e20;
        }

        .wechat-content p.list-highlight {
            background: none;
            border-left: none;
            padding: 0;
            border-radius: 0;
            color: rgb(29, 61, 34);
            margin-bottom: 16px;
        }

        .wechat-content p.list-highlight span.list-highlight-span {
            background: rgba(76, 175, 80, 0.10);
            border-left: 4px solid rgb(76, 175, 80);
            padding: 6px 12px;
            border-radius: 6px;
            color: rgb(29, 61, 34);
            margin-right: 6px;
        }
        """
