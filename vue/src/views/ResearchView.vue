<script setup lang="ts">
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import Abstract from '@/components/pages/Abstract.vue';
import References from '@/components/pages/References.vue';
import GambarComponent from '@/components/pages/GambarComponent.vue';
import Tabels from '@/components/pages/Tabels.vue';
import { Button } from '@/components/ui/button'

const downloadSkripsi = () => {
    window.open('/pdf/skripsi.pdf', '_blank')
}
</script>

<template>
    <Tabs default-value="abstrak" class="w-full">
        <TabsList>
            <TabsTrigger value="abstrak">
                Abstrak
            </TabsTrigger>
            <TabsTrigger value="referensi">
                Referensi
            </TabsTrigger>
            <TabsTrigger value="gambar">
                Gambar
            </TabsTrigger>
            <TabsTrigger value="tabel">
                Tabel
            </TabsTrigger>
            <TabsTrigger value="pdf">
                PDF Skripsi
            </TabsTrigger>
        </TabsList>
        <TabsContent value="abstrak" class="mt-4">
            <Abstract />
        </TabsContent>
        <TabsContent value="referensi" class="mt-4">
            <References />
        </TabsContent>
        <TabsContent value="gambar" class="mt-4">
           <GambarComponent/>
        </TabsContent>
        <TabsContent value="tabel" class="mt-4">
            <Tabels/>
        </TabsContent>
        <TabsContent value="pdf" class="mt-4">
            <div class="w-[50%]">
                <Button class="flex gap-3" @click="downloadSkripsi()">
                    <span>
                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m.75 12l3 3m0 0l3-3m-3 3v-6m-1.5-9H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9"/></svg>
                    </span>
                    Download
                </Button>
                <p class="font-semibold text-slate-400 italic mt-2">Last updated 29 April 2024</p>
            </div>
        </TabsContent>
    </Tabs>
</template>