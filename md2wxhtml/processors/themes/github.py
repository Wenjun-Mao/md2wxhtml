"""
GitHub-style theme.
Clean and familiar styling for developers and technical content.
"""

def get_css() -> str:
    """Get the GitHub theme CSS."""
    return """
        .wechat-content {
            background-color: #ffffff;
            color: #24292f;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
        }
        
        .wechat-content h1 {
            color: #24292f;
            border-bottom: 1px solid #d0d7de;
            padding-bottom: 10px;
            font-weight: 600;
        }
        
        .wechat-content h2 {
            color: #24292f;
            border-bottom: 1px solid #d0d7de;
            padding-bottom: 8px;
            font-weight: 600;
        }
        
        .wechat-content h3 {
            color: #24292f;
            font-weight: 600;
        }
        
        .wechat-content blockquote {
            border-left-color: #d0d7de;
            background-color: transparent;
            color: #656d76;
        }
        
        .wechat-content a {
            color: #0969da;
            border-bottom-color: #0969da;
        }
        
        .wechat-content strong {
            color: #24292f;
            font-weight: 600;
        }
        
        .wechat-content table th {
            background-color: #f6f8fa;
            border: 1px solid #d0d7de;
        }
        
        .wechat-content table td {
            border: 1px solid #d0d7de;
        }

        .wechat-content p.list-highlight {
            background: none;
            border-left: none;
            padding: 0;
            border-radius: 0;
            color: rgb(36, 41, 47);
            margin-bottom: 16px;
        }

        .wechat-content p.list-highlight span.list-highlight-span {
            background: rgba(9, 105, 218, 0.08);
            border-left: 4px solid rgb(9, 105, 218);
            padding: 6px 12px;
            border-radius: 6px;
            color: rgb(36, 41, 47);
            margin-right: 6px;
        }
        """
