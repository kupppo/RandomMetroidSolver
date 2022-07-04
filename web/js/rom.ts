import hasFileReader from './helpers/hasFileReader'
import Settings from './helpers/settings'

const VALID_EXTENSIONS = ['sfc', 'smc']

class VanillaROM {
  el: HTMLElement | null

  constructor() {
    if (!hasFileReader()) {
      alert('This website requires the HTML5 File API, please upgrade your browser to a newer version.')
      return
    }
    const settings = Settings()
    const selector = settings.permalink ? 'vanillaUploadFile' : 'uploadFile'
    this.el = document.getElementById(selector)
    const readFile = this.readFile.bind(this)
    this.el?.addEventListener('change', (evt: Event) => {
      const file = (<HTMLInputElement>evt.target).files?.[0]
      if (file) {
        readFile(file)
      }
    })
  }

  validateFileExtension(name: string) {
    const lastDot = name.lastIndexOf('.')
    const extension = name.substring(lastDot + 1).toLowerCase()
    if (VALID_EXTENSIONS.includes(extension)) {
      return true
    }
    throw Error(`Unsupported file extension: ${extension}`)
  }

  readFile(file: File) {
    this.validateFileExtension(file.name)
    console.log('valid file extension')
  }
}

export default VanillaROM
