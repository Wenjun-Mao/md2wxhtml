"""
Professional blue color scheme.
Ideal for business, technology, and corporate content.
"""

def get_css() -> str:
    """Get the Blue theme CSS."""
    return """
        .wechat-content {
            background-color: #f0f8ff;
            color: #1a365d;
        }
        
        .wechat-content h1 {
            color: #1e3a8a;
            border-bottom: 2px solid #3b82f6;
            padding-bottom: 5px;
        }
        
        .wechat-content h2 {
            color: #1d4ed8;
            border-bottom: 1px solid #60a5fa;
            padding-bottom: 3px;
        }
        
        .wechat-content h3 {
            color: #2563eb;
        }
        
        .wechat-content blockquote {
            border-left-color: #3b82f6;
            background-color: #dbeafe;
        }
        
        .wechat-content a {
            color: #1d4ed8;
            border-bottom-color: #3b82f6;
        }
        
        .wechat-content strong {
            color: #1e3a8a;
        }

        .wechat-content p.list-highlight {
            background: none;
            border-left: none;
            padding: 0;
            border-radius: 0;
            color: rgb(0, 0, 0);
            margin-bottom: 16px;
        }
        .wechat-content p.list-highlight span.list-highlight-span {
            background: rgba(30, 58, 138, 0.08);
            border-left: 4px solid rgb(30, 58, 138);
            padding: 6px 12px;
            border-radius: 6px;
            color: rgb(0, 0, 0);
            margin-right: 6px;
        }
        """
