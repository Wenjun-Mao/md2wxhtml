"""
Modern dark mode theme.
Eye-friendly dark styling with purple accents.
"""

def get_css() -> str:
    """Get the Dark theme CSS."""
    return """
        .wechat-content {
            background-color: #1a1a1a;
            color: #e4e4e7;
        }
        
        .wechat-content h1 {
            color: #fafafa;
            border-bottom: 2px solid #8b5cf6;
            padding-bottom: 5px;
        }
        
        .wechat-content h2 {
            color: #f4f4f5;
            border-bottom: 1px solid #a78bfa;
            padding-bottom: 3px;
        }
        
        .wechat-content h3 {
            color: #f4f4f5;
        }
        
        .wechat-content blockquote {
            border-left-color: #8b5cf6;
            background-color: #2d2d30;
            color: #a1a1aa;
        }
        
        .wechat-content a {
            color: #a78bfa;
            border-bottom-color: #8b5cf6;
        }
        
        .wechat-content strong {
            color: #fafafa;
        }
        
        .wechat-content table th {
            background-color: #2d2d30;
            color: #fafafa;
            border-color: #404040;
        }
        
        .wechat-content table td {
            border-color: #404040;
        }

        .wechat-content p.list-highlight {
            background: none;
            border-left: none;
            padding: 0;
            border-radius: 0;
            color: rgb(244, 244, 245);
            margin-bottom: 16px;
        }
        
        .wechat-content p.list-highlight span.list-highlight-span {
            background: rgba(139, 92, 246, 0.12);
            border-left: 4px solid rgb(139, 92, 246);
            padding: 6px 12px;
            border-radius: 6px;
            color: rgb(244, 244, 245);
            margin-right: 6px;
        }
        """
