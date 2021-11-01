import axios from 'axios'
import { URL } from './ApiBaseUrl'

const API = axios.create({
    baseURL: URL,
    timeout: 1000,
})

export { API as axios }