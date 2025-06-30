"""
Warm, paper-like background with soft colors.
"""

def get_css() -> str:
    """Get the Hammer theme CSS."""
    return """
        .wechat-content {
            background-color: #fbf7ee;
            color: #635753;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 
                         'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 
                         'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol',
                         'Noto Color Emoji';
            padding: 10px;
        }
        
        .wechat-content p {
            color: #635753;
            line-height: 2;
        }
        
        .wechat-content h1, .wechat-content h2, .wechat-content h3 {
            color: #635753;
        }
        
        .wechat-content a {
            color: #635753;
            border-bottom: 1px solid #ebdfd5;
        }
        
        .wechat-content strong {
            color: #635753;
        }
        
        .wechat-content em {
            color: #635753;
        }
        
        .wechat-content blockquote {
            color: #635753;
        }
        
        .wechat-content img {
            width: 100%;
            box-shadow: 14px 14px 28px #e6e6e6, -14px -14px 28px #fff;
            border: 9px solid #ffffff;
            outline: 1px solid #ebdfd5;
        }

        .wechat-content p.list-highlight {
            background: none;
            border-left: none;
            padding: 0;
            border-radius: 0;
            color: rgb(99, 87, 83);
            margin-bottom: 16px;
        }

        .wechat-content p.list-highlight span.list-highlight-span {
            background: rgba(235, 223, 213, 0.50);
            border-left: 4px solid rgb(99, 87, 8);
            padding: 6px 12px;
            border-radius: 6px;
            color: rgb(99, 87, 83);
            margin-right: 6px;
        }
        """