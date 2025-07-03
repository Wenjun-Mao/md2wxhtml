"""
Warm red color scheme.
"""

def get_css() -> str:
    return """
    .wechat-content {
        background: rgb(254,242,235);
    }
    .wechat-content p {
        color: rgb(0, 0, 0);
        line-height: 30px;
    }
    .wechat-content p.subtitle-paragraph {
        margin-top: 1em;  /* e.g., 20px or 1.5em */
        margin-bottom: 1em; /* e.g., 15px or 1em */
        }
    .wechat-content strong {
        color: rgb(220, 20, 60);
    }
    .wechat-content ul {
        background: transparent;
        margin: 10px;
    }
    .wechat-content img {
        width: 80%;
        border-radius: 10px;
    }
    .wechat-content h1 {
        color: rgb(220, 20, 60);
    }
    .wechat-content h2 {
        color: rgb(220, 20, 60);
        background: rgba(220, 20, 60, 0.08);
    }
    /* Remove highlight from the whole paragraph, only highlight the span */
    .wechat-content p.list-highlight {
        background: none;
        border-left: none;
        padding: 0;
        border-radius: 0;
        color: rgb(0, 0, 0);
        margin-bottom: 16px;
    }
    .wechat-content p.list-highlight span.list-highlight-span {
        background: rgba(220, 20, 60, 0.08);
        border-left: 4px solid rgb(220, 20, 60);
        padding: 6px 12px;
        border-radius: 6px;
        color: rgb(0, 0, 0);
        margin-right: 6px;
    }
    """
