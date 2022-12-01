import React, { useStart } from "react";


const DeletarNotaComponent = ({ dia, email, notaDia }) => {

    let emailEmpressa = email
    let diamesano = dia;
    let nota = notaDia;

    let corpoRequisicao = {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            dia_aser_adicionado: diamesano,
            email_da_empressa: emailEmpressa,
            nota_do_dia: nota
        })
    }


    const eventDeletarRota = () => {
        fetch('http://127.0.0.1:5000/DeletarDia', corpoRequisicao)
            .then((response) => response.json())
            .then((data) => console.log(data))
            .finally(console.log("Função Realizada"));
    }

    return (
        <div >
            <li>
                {/* <p>{emailEmpressa}</p> */}
                <p>{diamesano}</p>
                <p>{nota}</p>
            </li>
            <button onClick={eventDeletarRota}>Deletar nota especifico</button>
        </div>
    )
}

export default DeletarNotaComponent

