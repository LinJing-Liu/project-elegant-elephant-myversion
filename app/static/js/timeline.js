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
        let htmlSegment = `<div class="single-post row">
                                <div class="col-lg-2 col-md-2 col-sm-12">
                                    <img class="gravatar" src=${getGravatar(post.email)} />
                                </div>
                                <div class="col-lg-10 col-md-10 col-sm-12">
                                    <h2 class="name">${post.name}</h2>
                                    <div class="email"><a href="email:${post.email}">${post.email}</a></div>
                                    <div class="timestamp">${post.created_at}</a></div>
                                    <div class="content">${post.content}</div>
                                </div>
                            </div>
                            <hr class="post-divider" />`;
        html += htmlSegment;
    });

    let divElement = document.querySelector('.posts');
    divElement.innerHTML = html;
}

renderPosts();

function formSubmit() {
    let url = '/api/timeline_post';
    var request = new XMLHttpRequest();
    request.open('POST', url, true);
    request.onload = function() {
        console.log(request.responseText);
        if(request.status == 503) {
            alert("You have attempted to submit too many timeline requests at a time. Please try again later.");
        }
    };
 
    request.onerror = function() {
       console.log("issue connecting to api");
    };
 
    request.send(new FormData(event.target));
    renderPosts();
}
document.getElementById('postForm').addEventListener('submit', formSubmit);