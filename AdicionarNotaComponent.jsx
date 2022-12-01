
import { useState } from "react";

const AdicionarNotaComponent = () => {

    const [valorDia, setValorDia] = useState("01012000");
    const [valorNota, setValorNota] = useState("")

    let emailEmpressa = "teste@com.br"
    let diamesano = valorDia
    let nota = valorNota;

    let corpoRequisicao = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            dia_aser_adicionado: diamesano,
            email_da_empressa: emailEmpressa,
            nota_do_dia: nota
        })
    }


    const eventAdicionarDia = () => {
        fetch('http://127.0.0.1:5000/AdicionarDia', corpoRequisicao)
            .then((response) => response.json())
            .then((data) => console.log(data))
            .finally(console.log("Valores adicionado na tabela"));
    }

    const eventPuxarInputsDias = Event => {
        console.log("Valores dias mudados")
        setValorDia(Event.target.value)

        // console.log(this.diaAdicionado.value)
    }

    const eventPuxarInputsNotas = Event => {
        console.log("Valores de nota mudados")
        setValorNota(Event.target.value)

        // console.log(this.diaAdicionado.value)
    }

    return (
        <div >
            <form >
                <label>DIA:
                    <input
                        type="text"
                        value={valorDia}
                        onChange={eventPuxarInputsDias}
                    />
                </label>

                <label>NOTA:
                    <input
                        type="text"
                        value={valorNota}
                        onChange={eventPuxarInputsNotas}
                    />
                </label>

            </form>
            <button onClick={eventAdicionarDia}>Adicionar ao novo no Mes</button>
        </div>
    )
}

export default AdicionarNotaComponent;