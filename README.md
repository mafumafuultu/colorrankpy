# Color Rank

To get the most used colors in an image file

```py
import colors.rank as rk

imgpath = r'./sample.jpg'

rk.rank(imgpath, outpath=r'./test.json', top=10)
```

![sample image](./sample.jpg)

[sample image](https://pixabay.com/ja/photos/%E3%83%AC%E3%82%B9%E3%83%88%E3%83%A9%E3%83%B3-%E9%A3%9F%E5%93%81-%E3%83%86%E3%83%BC%E3%83%96%E3%83%AB-%E6%B5%B7-5521372/)

output

```json
[
    {
        "color": [
            "rgb(191, 174, 156)"
        ],
        "count": "667",
        "rank": 1
    },
    {
        "color": [
            "rgb(0, 122, 163)"
        ],
        "count": "607",
        "rank": 2
    },
    {
        "color": [
            "rgb(190, 173, 155)",
            "rgb(193, 176, 158)"
        ],
        "count": "594",
        "rank": 3
    },
    {
        "color": [
            "rgb(192, 175, 157)"
        ],
        "count": "577",
        "rank": 4
    },
    {
        "color": [
            "rgb(108, 177, 210)"
        ],
        "count": "495",
        "rank": 5
    },
    {
        "color": [
            "rgb(107, 177, 211)"
        ],
        "count": "492",
        "rank": 6
    },
    {
        "color": [
            "rgb(109, 178, 211)",
            "rgb(110, 179, 212)"
        ],
        "count": "491",
        "rank": 7
    },
    {
        "color": [
            "rgb(191, 171, 147)"
        ],
        "count": "487",
        "rank": 8
    },
    {
        "color": [
            "rgb(106, 176, 210)"
        ],
        "count": "481",
        "rank": 9
    },
    {
        "color": [
            "rgb(191, 173, 153)"
        ],
        "count": "470",
        "rank": 10
    }
]
```