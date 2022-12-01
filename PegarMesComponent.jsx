import React, { useState } from 'react';

import DeletarNotaComponent from "./DeletarNotaComponent"

const PegarMesComponent = () => {

    let [listaTodosValores, setlistaTodosValores] = useState([{ Dia: "1132022", Email: "teste@com.br", Nota: "hackermnan 23 a saga continua lllljmipoefion" }])


    let corpoRequisicao = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email_da_empressa: "teste@com.br" })
    }


    // async function PegarTudoMesComEmail() {
    //     const eventRotaPegarTodoMes = () => {
    //         fetch('http://127.0.0.1:5000/todomes', corpoRequisicao)
    //             .then((response) => response.json())
    //             .then((data) => console.log(listaTodosValores = data))
    //             .finally(console.log(listaTodosValores));
    //     }

    // }

    // async function PegarTudoMesComEmail() {
    //     const eventRotaPegarTodoMes = await
    //         fetch('http://127.0.0.1:5000/todomes', corpoRequisicao)
    //             .then((response) => response.json())

    //     listaTodosValores = eventRotaPegarTodoMes
    //     console.log(listaTodosValores)
    // }



    async function PegarTudoMesComEmail() {
        await fetch('http://127.0.0.1:5000/todomes', corpoRequisicao)
            .then((response) => response.json())
            .then((data) => setlistaTodosValores(data))

        console.log(listaTodosValores)
    }


    // useEffect(() => {
    //     fetch('http://127.0.0.1:5000/todomes', corpoRequisicao)
    //         .then((response) => response.json())
    //         .then((data) => setlistaTodosValores(data))
    // })


    // PegarTudoMesComEmail()

    // const eventMostraListaPegos = () => {
    //     console.log(listaTodosValores)
    //     const ListaTesteMap = listaTodosValores.map((x) => <p>{x["dia"]}</p>)
    //     console.log(ListaTesteMap)
    // }



    return (
        // <div onLoad={eventRotaPegarTodoMes()}>
        <div>
            <button onClick={PegarTudoMesComEmail}>Pegar todo Mes</button>
            <div>
                {listaTodosValores.map(
                    notaDeleteComp => <DeletarNotaComponent dia={notaDeleteComp.Dia} email={notaDeleteComp.Email} notaDia={notaDeleteComp.Nota} />)}

            </div>


        </div>
    )
}

export default PegarMesComponent;