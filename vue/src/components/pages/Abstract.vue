<script setup lang="ts">
import {
    Card,
    CardContent,
    CardFooter,
    CardHeader,
    CardTitle,
} from '@/components/ui/card'
</script>

<template>
    <Card>
        <CardHeader>
            <CardTitle>
                Penentuan Keterikatan Tekstual Dalam Surat
                Kontrak Bertipe NDA (Non-Disclosure Agreement) Menggunakan ALBERT (A
                Lite BERT)
            </CardTitle>
        </CardHeader>
        <CardContent class="text-justify">
            &nbsp; NDA (Non-Disclosure Agreement) merupakan salah satu tipe surat kontrak.
            NDA mengikat dua atau lebih pihak dimana semuanya setuju bahwa informasi
            tertentu yang dibagikan atau dibuat satu pihak bersifat rahasia. Kontrak ini
            berfungsi untuk melindungi informasi sensitif, menjaga hak paten, dan mengontrol
            informasi yang dibagikan.Membaca dan memahami surat kontrak adalah proses
            yang repetitif, memakan banyak waktu dan tenaga. Walau begitu, aktivitas tersebut
            masih sangat krusial dalam dunia bisnis, karena dapat mengikat dua atau lebih pihak
            dibawah hukum. Masalah ini sangat cocok untuk dikerjakan oleh Artificial
            Intelegence menggunakan Deep Learning.Oleh karena itu, penelitian ini bertujuan
            untuk menguji dan mengembangkan pretrained language model yang didesain
            khusus untuk memahami surat kontrak. Metode yang digunakan adalah melatih
            model untuk melakukan tugas inferensi bahasa berupa textual entailment dengan
            dataset ContractNLI.Hasilnya, model ALBERT-base yang digunakan menunjukan
            skor akurasi sebesar 85,0 dan skor F1 makro sebesar 82,4. Walaupun nilai ini tidak
            menjadi State of The Art dari benchmark ContractNLI, model yang dilatih masih
            bisa mengalahkan beberapa model lain yang memiliki parameter jauh lebih besar.
        </CardContent>
        <CardFooter>
            Kata Kunci: NLI, ALBERT, Textual Entailment, NLP, Contract, Finetuning,
            NDA, Deep Learning, Language Model.
        </CardFooter>
    </Card>
</template>