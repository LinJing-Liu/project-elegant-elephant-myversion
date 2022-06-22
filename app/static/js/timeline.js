function getGravatar(email)
{
    var base = "http://www.gravatar.com/avatar/";
    var hash = CryptoJS.MD5(email);
    var fullUrl = base+hash +"?d=identicon&s=64";
    return fullUrl;
}

async function getPosts() {
    let url = '/api/timeline_post';
    try {
        let res = await fetch(url);
        return await res.json();
    } catch (error) {
        console.log(error);
    }
}

async function renderPosts() {
    let posts = await getPosts();
    let html = '';
    posts.timeline_posts.forEach(post => {
        let htmlSegment = `<div class="singlePost">
                            <img class="gravatar" src=${getGravatar(post.email)} />
                            <h2>${post.name}</h2>
                            <div class="email"><a href="email:${post.email}">${post.email}</a></div>
                            <div class="timestamp">${post.created_at}</a><div>
                            <div class="content">${post.content}</div>
                            <br />
                        </div>`;
        html += htmlSegment;
    });

    let divElement = document.querySelector('.posts');
    divElement.innerHTML = html;
}

renderPosts();

function formSubmit() {
    event.preventDefault();

    let url = '/api/timeline_post';
    var request = new XMLHttpRequest();
    request.open('POST', url, true);
    request.onload = function() {
       console.log(request.responseText);
    };
 
    request.onerror = function() {
       console.log("issue connecting to api");
    };
 
    request.send(new FormData(event.target));
    renderPosts();
}
document.getElementById('postForm').addEventListener('submit', formSubmit);