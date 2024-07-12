function OpenSideNav() {
    document.getElementById("mainpage-sidenav").style.width = "250px"
    document.getElementById("content").style.marginLeft = "250px"
}

function CloseSideNav() {
    document.getElementById("mainpage-sidenav").style.width = "0"
    document.getElementById("content").style.marginLeft = "0"
}


document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("open-sidenav").addEventListener('click', OpenSideNav)
})