import { ref, computed, watch } from 'vue'
import { defineStore } from 'pinia'

export const useAnalyzeStore = defineStore('analyze', () => {
    const result = ref('')
    const error = ref(false)
    const history = ref<
        {
            timestamp: string,
            result: string,
        }[]
    >([])

    async function analyzePair(contract: string, hypothesis: string) {
        // Send a request to the server to get the hypos
        const response = await fetch('http://127.0.0.1:8000/model/customanalyze/', {
                method: 'POST',
                headers: {
                        'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                        contract,
                        hypothesis,
                }),
        });

        // Check if the request was successful
        if (!response.ok) {
            error.value = true;
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response body as JSON
        const data = await response.json();

        // Update the result state
        result.value = data;
    }

    function addToHistory() {
        history.value.push({
            timestamp: new Date().toISOString(),
            result: result.value,
        })
    }

    function clearHistory() {
        history.value = []
    }

    function getHistoryFromLocalStorage() {
        const historyFromLocalStorage = localStorage.getItem('history')
        if (historyFromLocalStorage) {
            history.value = JSON.parse(historyFromLocalStorage)
        }
    }


    //watch history and save it to local storage
    watch(history, () => {
        localStorage.setItem('history', JSON.stringify(history.value))
    }, { deep: true })

    return { result, analyzePair, error, history, addToHistory, clearHistory, getHistoryFromLocalStorage}
})
