document.addEventListener("DOMContentLoaded", () => {
    // ---- Lógica do Modal do Cardápio ----
    const modal = document.getElementById("sorveteModal");
    const spanClose = document.querySelector(".close");
    const items = document.querySelectorAll(".cardapio-item");
    const dataScript = document.getElementById("sorvetes-data");

    if (modal && dataScript) {
        // Lê os dados inseridos pelo Django no HTML
        const sorvetesData = JSON.parse(dataScript.textContent);

        // Adiciona evento de clique em cada card de sorvete
        items.forEach(item => {
            item.addEventListener("click", function() {
                const index = this.getAttribute("data-index");
                const sorvete = sorvetesData[index];

                // Preenche o modal
                document.getElementById("modal-img").src = sorvete.img;
                document.getElementById("modal-titulo").textContent = sorvete.titulo;
                document.getElementById("modal-desc").textContent = sorvete.desc;
                document.getElementById("modal-preco").textContent = sorvete.preco;

                // Mostra o modal com animação
                modal.classList.add("show");
            });
        });

        // Fechar modal ao clicar no 'X'
        spanClose.onclick = function() {
            modal.classList.remove("show");
        }

        // Fechar modal ao clicar fora dele
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.classList.remove("show");
            }
        }
    }
});

// Mantém a função global caso esteja sendo chamada no HTML
function fecharModal() {
    const modal = document.getElementById("sorveteModal");
    if(modal) modal.classList.remove("show");
}