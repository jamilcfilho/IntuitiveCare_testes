<template>
  <div id="app">
    <h1>Busca de Operadoras</h1>
    <input v-model="query" type="text" placeholder="Digite o nome ou CNPJ da operadora" />
    <button @click="buscar">Buscar</button>

    <div v-if="resultados.length > 0">
      <h2>Resultados:</h2>
      <ul>
        <li v-for="(item, index) in resultados" :key="index">
          {{ item.Razao_Social }} - {{ item.CNPJ }}
        </li>
      </ul>
    </div>
    <div v-else>
      <p>Nenhum resultado encontrado.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      query: '',
      resultados: []
    };
  },
  methods: {
    buscar() {
      // Fazendo uma requisição GET para a API Flask
      axios
        .get(`http://localhost:5000/buscar?query=${this.query}`)
        .then(response => {
          // Armazenando os dados recebidos na variável 'resultados'
          this.resultados = response.data;
        })
        .catch(error => {
          console.error("Erro ao buscar dados:", error);
        });
    }
  }
};
</script>
