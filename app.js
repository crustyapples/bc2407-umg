const express = require('express');
const app = express();
const cookieParser = require('cookie-parser');
const cors = require('cors');

app.use(cookieParser());
app.use(cors());
app.listen(process.env.PORT || 3000).

CLIENT_SECRET = "6d6241200b65a93598c886df7b29ed58"
CLIENT_KEY = "aw1i93ole5ii0jbm"
SERVER_ENDPOINT_REDIRECT = "https://www.tiktok.com/auth/authorize"

app.get('/oauth', (req, res) => {
    const csrfState = Math.random().toString(36).substring(2);
    res.cookie('csrfState', csrfState, { maxAge: 60000 });

    let url = 'https://www.tiktok.com/auth/authorize/';

    url += '?client_key=' + CLIENT_KEY;
    url += '&scope=user.info.basic,video.list';
    url += '&response_type=code';
    url += '&redirect_uri=' + SERVER_ENDPOINT_REDIRECT;
    url += '&state=' + csrfState;

    console.log(url)
    res.redirect(url);
})

app.get('/redirect', (req, res) => {
    console.log(req.query)
    const { code, state } = req.query;
    const { csrfState } = req.cookies;

    if (state !== csrfState) {
        res.status(422).send('Invalid state');
        return;
    }

    let url_access_token = 'https://open-api.tiktok.com/oauth/access_token/';
    url_access_token += '?client_key=' + "aw1i93ole5ii0jbm";
    url_access_token += '&client_secret=' + "6d6241200b65a93598c886df7b29ed58";
    url_access_token += '&code=' + code;
    url_access_token += '&grant_type=authorization_code';

    console.log(url_access_token)

    fetch(url_access_token, {method: 'post'})
        .then(res => res.json())
        .then(json => {
            console.log("hello",json)
            res.send(json);
        });
})