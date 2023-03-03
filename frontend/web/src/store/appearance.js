import { defineStore } from 'pinia'

export const appearance = defineStore('apprearance', {
    state() {
        return {
            collapsed: parseInt(localStorage.getItem('sidebarCollapsed')) === 1
        }
    },

    actions: {
        setSidebarCollapsed(status) {
            console.log("collapsed", status)
            this.collapsed = status;
            localStorage.setItem('sidebarCollapsed', status ? 1 : 0)
        },

        isSidebarCollapased() {
            console.log("collap", this.collapsed)
            return this.collapsed
        }
    }
})
1