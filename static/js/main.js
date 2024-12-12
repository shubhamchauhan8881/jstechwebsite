const HidePopUp = () => {
    document.querySelector("#popup").classList.add("hidden");
}

function Fetch(url){
    
    ShowDialog("<p class='p-8 text-xl'>Loading..</p>");

    fetch(`/get-page/${url}`)
      .then(response => response.text())
      .then(data => {if(modal.open) ShowDialog(data);} )
      .catch(err => ShowDialog(err.message));
}


document.addEventListener("DOMContentLoaded", () => {

    setTimeout(() =>document.getElementById("loader").style.display = "none", 300);
    
    const modal = document.querySelector("#modal");

    function ShowDialog(content){
        modal.show();
        document.querySelector("#modal-content").innerHTML = content;
    }

    modal.addEventListener("click", e=>{ if(e.target == document.querySelector("#modal-backlayer"))modal.close();})

});

