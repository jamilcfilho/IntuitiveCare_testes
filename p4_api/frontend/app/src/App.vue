<template>
  <div id="app" class="container">
    <div class="search-container">
      <h1>Busca de Operadoras</h1>
      <input
        v-model="query"
        @input="buscarOperadora"
        type="text"
        placeholder="Digite o nome ou CNPJ da operadora"
        class="search-input"
      />
      <ul v-if="resultados.length">
        <li v-for="(resultado, index) in resultados" :key="index" class="resultado-item">
          <p><strong>Razão Social:</strong> {{ resultado.Razao_Social }}</p>
          <p><strong>CNPJ:</strong> {{ resultado.CNPJ }}</p>
          <p><strong>Cidade:</strong> {{ resultado.Cidade }} - {{ resultado.UF }}</p>
        </li>
      </ul>
      <p v-if="resultados.length === 0 && query">Nenhum resultado encontrado.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      query: '',
      resultados: []
    };
  },
  methods: {
    buscarOperadora() {
      if (this.query.length > 2) {
        fetch(`http://localhost:5000/buscar?query=${this.query}`)
          .then((response) => response.json())
          .then((data) => {
            this.resultados = data;
          })
          .catch((error) => {
            console.error("Erro na busca:", error);
          });
      } else {
        this.resultados = [];
      }
    }
  }
};
</script>

<style scoped>
/* Reset básico */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Corpo da página */
body {
  font-family: 'Arial', sans-serif;
  background-color: #e7f4f8; /* Tom suave de fundo */
  color: #333;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}

/* Container principal */
.container {
  width: 100%;
  max-width: 600px;
  padding: 30px;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

/* Título */
h1 {
  text-align: center;
  color: #4a4a4a;
  font-size: 28px;
  margin-bottom: 20px;
  font-weight: bold;
}

/* Campo de busca */
.search-container {
  text-align: center;
}

/* Estilo do input */
.search-input {
  width: 100%;
  padding: 12px;
  margin-bottom: 20px;
  border: 1px solid #dcdcdc;
  border-radius: 6px;
  font-size: 16px;
  background-color: #f0f8ff; /* Cor de fundo mais clara */
  color: #333;
  transition: background-color 0.3s ease;
}

.search-input:focus {
  background-color: #e1eff7; /* Fundo um pouco mais intenso no foco */
  outline: none;
}

/* Estilo da lista de resultados */
ul {
  list-style: none;
  padding: 0;
}

.resultado-item {
  background-color: #f9fafb; /* Cor de fundo suave */
  border: 1px solid #dcdcdc;
  border-radius: 6px;
  margin-bottom: 15px;
  padding: 15px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Tamanho e estilo dos itens de resultado */
.resultado-item p {
  margin: 8px 0;
  font-size: 16px;
}

/* Mensagem caso não tenha resultados */
p {
  text-align: center;
  color: #888;
}
</style>
