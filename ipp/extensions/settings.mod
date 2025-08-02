// JSON basic
{
    "name": "IPP Settings",
    "description": "Stardard settings for IPP",
    "use_in": [
        "gdstu.ipp",
        "gdstu.update_log"
    ],
    "profile": "/todo.py",
    "info": {
        "app_name": "Winux",
        "ver": "2025070513",
        "version": "Winux-rd_2025070513"
    },
    "config": {
        "app": "/__init__.py",
        "apps": [
            "/__main__.py",
            "/__init__.py",
        ],
        "dirs": [],
        "git": true,
        "gitignore": true,
        "enable_api": true,
        "api": false,
        // Cannot show the API key with {"gitignore": true}
        "apis": false
        // Cannot show the API keys with {"gitignore": true}
    },
    "debug": true
}