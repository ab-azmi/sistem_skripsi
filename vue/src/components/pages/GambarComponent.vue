<script setup lang="ts">
import { ref } from 'vue'
import { watchOnce } from '@vueuse/core'
import { Carousel, type CarouselApi, CarouselContent, CarouselItem, CarouselNext, CarouselPrevious } from '@/components/ui/carousel'
import { Card, CardContent } from '@/components/ui/card'

const emblaMainApi = ref<CarouselApi>()
const emblaThumbnailApi = ref<CarouselApi>()
const selectedIndex = ref(0)

const images = [
    {
        index: 0,
        url: '/images/research/alur.png',
        caption: 'Flowchart metode penelitian',
        alt: 'flowchart'
    },
    {
        index: 1,
        url: '/images/research/arsitektur.png',
        caption: 'Arsitektur ALBERT',
        alt: 'arsitektur'
    },
    {
        index: 2,
        url: '/images/research/distribusi_kata_hypo.png',
        caption: 'Distribusi kata pada hipotesis',
        alt: 'distribusi kata'
    },
    {
        index: 3,
        url: '/images/research/jumlah_kata_premis.png',
        caption: 'Distribusi kata pada premis',
        alt: 'distribusi kata'
    },
    {
        index: 4,
        url: '/images/research/embedding.png',
        caption: 'Embedding kata 4 dimensi',
        alt: 'embedding'
    },
    {
        index: 5,
        url: '/images/research/json.png',
        caption: 'Format JSON dari dataset CNLI',
        alt: 'JSON CNLI'
    },
    {
        index: 6,
        url: '/images/research/jumlah_label.png',
        caption: 'Distribusi jumlah kata per-label pada dataset CNLI',
        alt: 'distribusi label'
    },
    {
        index: 7,
        url: '/images/research/label_hipotesis.png',
        caption: 'Distribusi label pada hipotesis',
        alt: 'distribusi label hipotesis'
    },
    {
        index: 8,
        url: '/images/research/load_model.png',
        caption: 'Source code to load model ALBERT',
        alt: 'load model'
    },
    {
        index: 9,
        url: '/images/research/NLI.png',
        caption: 'Area penelitian pada Natural Language Inference',
        alt: 'NLI'
    },
    {
        index: 10,
        url: '/images/research/optim.png',
        caption: 'Source code untuk optimasi model ALBERT',
        alt: 'optimasi model'
    },
    {
        index: 11,
        url: '/images/research/perkembangan.png',
        caption: 'Perkembangan dalam NLP sejak 2001-sekarang',
        alt: 'hasil uji coba 5'
    },
    {
        index: 12,
        url: '/images/research/pseudocode_all.png',
        caption: 'Pseudocode dari keseluruhan metode penelitian',
        alt: 'pseudocode all'
    },
    {
        index: 13,
        url: '/images/research/pseudocode_training.png',
        caption: 'Pseudocode dari proses training',
        alt: 'pseudocode training'
    },
    {
        index: 14,
        url: '/images/research/result_confuse.png',
        caption: 'Confusion matrix dari hasil uji coba',
        alt: 'hasil uji coba'
    },
    {
        index: 15,
        url: '/images/research/sample.png',
        caption: 'Contoh data pada dataset CNLI',
        alt: 'sample'
    },
    {
        index: 16,
        url: '/images/research/schedule.png',
        caption: 'Warm up steps pada proses training',
        alt: 'step training'
    },
    {
        index: 17,
        url: '/images/research/splitting.png',
        caption: 'Pembagian data pada dataset CNLI',
        alt: 'splitting data'
    },
    {
        index: 18,
        url: '/images/research/token_premis.png',
        caption: 'Distribusi token pada premis',
        alt: 'distribusi token premis'
    },
    {
        index: 19,
        url: '/images/research/transformer.png',
        caption: 'Arsitektur Transformer',
        alt: 'transformer'
    }
]

function onSelect() {
    if (!emblaMainApi.value || !emblaThumbnailApi.value)
        return
    selectedIndex.value = emblaMainApi.value.selectedScrollSnap()
    emblaThumbnailApi.value.scrollTo(emblaMainApi.value.selectedScrollSnap())
}

function onThumbClick(index: number) {
    if (!emblaMainApi.value || !emblaThumbnailApi.value)
        return
    emblaMainApi.value.scrollTo(index)
}

watchOnce(emblaMainApi, (emblaMainApi) => {
    if (!emblaMainApi)
        return

    onSelect()
    emblaMainApi.on('select', onSelect)
    emblaMainApi.on('reInit', onSelect)
})
</script>

<template>
    <div class="w-[50%]">
        <Carousel class="relative w-full max-w-xl m-auto" @init-api="(val) => emblaMainApi = val">
            <CarouselContent>
                <CarouselItem v-for="img in images" :key="img.index">
                    <div class="p-1">
                        <Card>
                            <CardContent class="flex flex-col aspect-square items-center justify-center p-6">

                                <img :src="img.url" :alt="img.alt" class="w-full h-full object-contain" />
                                <span>{{ img.caption }}</span>
                            </CardContent>
                        </Card>
                    </div>
                </CarouselItem>
            </CarouselContent>
            <CarouselPrevious />
            <CarouselNext />
        </Carousel>

        <Carousel class="relative w-full max-w-xs m-auto" @init-api="(val) => emblaThumbnailApi = val">
            <CarouselContent class="flex gap-1 ml-0">
                <CarouselItem v-for="img in images" :key="img.index" class="pl-0 basis-1/4 cursor-pointer"
                    @click="onThumbClick(img.index)">
                    <div class="p-1" :class="img.index === selectedIndex ? '' : 'opacity-50'">
                        <Card>
                            <CardContent class="flex aspect-square items-center justify-center p-6">
                                <span class="text-4xl font-semibold">{{ img.index + 1 }}</span>
                            </CardContent>
                        </Card>
                    </div>
                </CarouselItem>
            </CarouselContent>
        </Carousel>
    </div>

</template>