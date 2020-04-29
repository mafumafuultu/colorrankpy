# Color Rank

To get the most used colors in an image file

```py
import colors.rank as rk

imgpath = r'./sample.png'

rk.rank(imgpath, outpath=r'./test.json', top=10)
```

output

```json
[
        {
        "rank": 1,
        "count": "12588",
        "color": [
            "rgb(244, 242, 233)"
        ]
    },
    {
        "rank": 2,
        "count": "1561",
        "color": [
            "rgb(253, 253, 253)"
        ]
    },
    {
        "rank": 3,
        "count": "1186",
        "color": [
            "rgb(237, 235, 226)"
        ]
    },
    {
        "rank": 4,
        "count": "1160",
        "color": [
            "rgb(216, 84, 52)"
        ]
    },
    {
        "rank": 5,
        "count": "657",
        "color": [
            "rgb(218, 85, 52)"
        ]
    }
]
```