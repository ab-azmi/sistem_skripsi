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
        url: '/images/research/tables/contoh_hyper.png',
        caption: 'Contoh Hyperparameter',
        alt: 'contoh hyperparameter'
    },
    {
        index: 1,
        url: '/images/research/tables/eksperimen_1.png',
        caption: 'Hasil eksperimen dengan 1 layer group',
        alt: 'eksperimen 1'
    },
    {
        index: 2,
        url: '/images/research/tables/eksperimen_2.png',
        caption: 'Hasil eksperimen dengan 3 layer group',
        alt: 'eksperimen 2'
    },
    {
        index: 3,
        url: '/images/research/tables/hasil_1.png',
        caption: 'Hasil akurasi dibandingkan dengan SpanNLI-BERT',
        alt: 'hasil 1'
    },
    {
        index: 4,
        url: '/images/research/tables/hasil_2.png',
        caption: 'Hasil Exact Match (EM) dibandingkan dengan model lain',
        alt: 'hasil 2'
    },
    {
        index: 5,
        url: '/images/research/tables/hyper.png',
        caption: 'Hyperparameter yang digunakan pada eksperimen',
        alt: 'hyperparameter'
    },
    {
        index: 6,
        url: '/images/research/tables/perbandingan.png',
        caption: 'Perbandingan model ALBERT dan BERT',
        alt: 'perbandingan model'
    },
    {
        index: 7,
        url: '/images/research/tables/sample_kasus.png',
        caption: 'Contoh kasus textual entailment',
        alt: 'contoh kasus'
    },
    {
        index: 8,
        url: '/images/research/tables/sumber_data.png',
        caption: 'Sumber data yang digunakan dalam penelitian',
        alt: 'sumber data'
    },
    
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
                            <CardContent class="flex flex-col aspect-square h-80 w-full items-center justify-center p-6">

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