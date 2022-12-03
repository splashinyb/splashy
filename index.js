const PORT = 8000
const express = require("express")
const axios = require("axios")
const cheerio = require("cheerio")
const { response } = require("express")

const app = express()

const url = 'https://www.theguardian.com/us'

axios(url).then(response => {
    const html = response.data
    const $ = cheerio.load(html)
    const articles = []
    $('.fc-item__title', html).each(function() {
        const title = $(this).text()
        const url = $(this).find('a').attr('href')
        console.log(title)
        console.log(url)
        articles.push({
            title,
            url
        })
    })
    console.log(articles)
}).catch(err => console.log(err))


app.listen(PORT, () => console.log(`server running on PORT ${PORT}`))

