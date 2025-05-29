import os
from .utils import run_command

PIPER_MODELS = {
    "ar_JO": {
        "kareem": ["ar_JO-kareem-low", "ar_JO-kareem-medium"]
    },
    "ca_ES": {
        "upc_ona": ["ca_ES-upc_ona-x_low", "ca_ES-upc_ona-medium"],
        "upc_pau": ["ca_ES-upc_pau-x_low"]
    },
    "cs_CZ": {
        "jirka": ["cs_CZ-jirka-low", "cs_CZ-jirka-medium"]
    },
    "cy_GB": {
        "bu_tts": ["cy_GB-bu_tts-medium"],
        "gwryw_gogleddol": ["cy_GB-gwryw_gogleddol-medium"]
    },
    "da_DK": {
        "talesyntese": ["da_DK-talesyntese-medium"]
    },
    "de_DE": {
        "eva_k": ["de_DE-eva_k-x_low"],
        "karlsson": ["de_DE-karlsson-low"],
        "kerstin": ["de_DE-kerstin-low"],
        "mls": ["de_DE-mls-medium"],
        "pavoque": ["de_DE-pavoque-low"],
        "ramona": ["de_DE-ramona-low"],
        "thorsten": ["de_DE-thorsten-low", "de_DE-thorsten-medium", "de_DE-thorsten-high"],
        "thorsten_emotional": ["de_DE-thorsten_emotional-medium"]
    },
    "el_GR": {
        "rapunzelina": ["el_GR-rapunzelina-low"]
    },
    "en_GB": {
        "alan": ["en_GB-alan-low", "en_GB-alan-medium"],
        "alba": ["en_GB-alba-medium"],
        "aru": ["en_GB-aru-medium"],
        "cori": ["en_GB-cori-medium", "en_GB-cori-high"],
        "jenny_dioco": ["en_GB-jenny_dioco-medium"],
        "northern_english_male": ["en_GB-northern_english_male-medium"],
        "semaine": ["en_GB-semaine-medium"],
        "southern_english_female": ["en_GB-southern_english_female-low"],
        "vctk": ["en_GB-vctk-medium"]
    },
    "en_US": {
        "amy": ["en_US-amy-low", "en_US-amy-medium"],
        "arctic": ["en_US-arctic-medium"],
        "bryce": ["en_US-bryce-medium"],
        "danny": ["en_US-danny-low"],
        "hfc_female": ["en_US-hfc_female-medium"],
        "hfc_male": ["en_US-hfc_male-medium"],
        "joe": ["en_US-joe-medium"],
        "john": ["en_US-john-medium"],
        "kathleen": ["en_US-kathleen-low"],
        "kristin": ["en_US-kristin-medium"],
        "kusal": ["en_US-kusal-medium"],
        "l2arctic": ["en_US-l2arctic-medium"],
        "lessac": ["en_US-lessac-low", "en_US-lessac-medium", "en_US-lessac-high"],
        "libritts": ["en_US-libritts-high"],
        "libritts_r": ["en_US-libritts_r-medium"],
        "ljspeech": ["en_US-ljspeech-medium", "en_US-ljspeech-high"],
        "norman": ["en_US-norman-medium"],
        "reza_ibrahim": ["en_US-reza_ibrahim-medium"],
        "ryan": ["en_US-ryan-low", "en_US-ryan-medium", "en_US-ryan-high"],
        "sam": ["en_US-sam-medium"]
    },
    "es_ES": {
        "carlfm": ["es_ES-carlfm-x_low"],
        "davefx": ["es_ES-davefx-medium"],
        "mls_10246": ["es_ES-mls_10246-low"],
        "mls_9972": ["es_ES-mls_9972-low"],
        "sharvard": ["es_ES-sharvard-medium"]
    },
    "es_MX": {
        "ald": ["es_MX-ald-medium"],
        "claude": ["es_MX-claude-high"]
    },
    "fa_IR": {
        "amir": ["fa_IR-amir-medium"],
        "ganji": ["fa_IR-ganji-medium"],
        "ganji_adabi": ["fa_IR-ganji_adabi-medium"],
        "gyro": ["fa_IR-gyro-medium"],
        "reza_ibrahim": ["fa_IR-reza_ibrahim-medium"]
    },
    "fi_FI": {
        "harri": ["fi_FI-harri-low", "fi_FI-harri-medium"]
    },
    "fr_FR": {
        "gilles": ["fr_FR-gilles-low"],
        "mls": ["fr_FR-mls-medium"],
        "mls_1840": ["fr_FR-mls_1840-low"],
        "siwis": ["fr_FR-siwis-low", "fr_FR-siwis-medium"],
        "tom": ["fr_FR-tom-medium"],
        "upmc": ["fr_FR-upmc-medium"]
    },
    "hu_HU": {
        "anna": ["hu_HU-anna-medium"],
        "berta": ["hu_HU-berta-medium"],
        "imre": ["hu_HU-imre-medium"]
    },
    "is_IS": {
        "bui": ["is_IS-bui-medium"],
        "salka": ["is_IS-salka-medium"],
        "steinn": ["is_IS-steinn-medium"],
        "ugla": ["is_IS-ugla-medium"]
    },
    "it_IT": {
        "paola": ["it_IT-paola-medium"],
        "riccardo": ["it_IT-riccardo-x_low"]
    },
    "ka_GE": {
        "natia": ["ka_GE-natia-medium"]
    },
    "kk_KZ": {
        "iseke": ["kk_KZ-iseke-x_low"],
        "issai": ["kk_KZ-issai-high"],
        "raya": ["kk_KZ-raya-x_low"]
    },
    "lb_LU": {
        "marylux": ["lb_LU-marylux-medium"]
    },
    "lv_LV": {
        "aivars": ["lv_LV-aivars-medium"]
    },
    "ml_IN": {
        "arjun": ["ml_IN-arjun-medium"],
        "meera": ["ml_IN-meera-medium"]
    },
    "ne_NP": {
        "google": ["ne_NP-google-x_low", "ne_NP-google-medium"]
    },
    "nl_BE": {
        "nathalie": ["nl_BE-nathalie-x_low", "nl_BE-nathalie-medium"],
        "rdh": ["nl_BE-rdh-x_low", "nl_BE-rdh-medium"]
    },
    "nl_NL": {
        "mls": ["nl_NL-mls-medium"],
        "mls_5809": ["nl_NL-mls_5809-low"],
        "mls_7432": ["nl_NL-mls_7432-low"],
        "pim": ["nl_NL-pim-medium"],
        "ronnie": ["nl_NL-ronnie-medium"]
    },
    "no_NO": {
        "talesyntese": ["no_NO-talesyntese-medium"]
    },
    "pl_PL": {
        "darkman": ["pl_PL-darkman-medium"],
        "gosia": ["pl_PL-gosia-medium"],
        "mc_speech": ["pl_PL-mc_speech-medium"],
        "mls_6892": ["pl_PL-mls_6892-low"]
    },
    "pt_BR": {
        "cadu": ["pt_BR-cadu-medium"],
        "edresson": ["pt_BR-edresson-low"],
        "faber": ["pt_BR-faber-medium"],
        "jeff": ["pt_BR-jeff-medium"]
    },
    "pt_PT": {
        "tugão": ["pt_PT-tugão-medium"]  # 保留原文特殊字符（如变音符号）
    },
    "ro_RO": {
        "mihai": ["ro_RO-mihai-medium"]
    },
    "ru_RU": {
        "denis": ["ru_RU-denis-medium"],
        "dmitri": ["ru_RU-dmitri-medium"],
        "irina": ["ru_RU-irina-medium"],
        "ruslan": ["ru_RU-ruslan-medium"]
    },
    "sk_SK": {
        "lili": ["sk_SK-lili-medium"]
    },
    "sl_SI": {
        "artur": ["sl_SI-artur-medium"]
    },
    "sr_RS": {
        "serbski_institut": ["sr_RS-serbski_institut-medium"]
    },
    "sv_SE": {
        "lisa": ["sv_SE-lisa-medium"],
        "nst": ["sv_SE-nst-medium"]
    },
    "sw_CD": {
        "lanfrica": ["sw_CD-lanfrica-medium"]
    },
    "tr_TR": {
        "dfki": ["tr_TR-dfki-medium"],
        "fahrettin": ["tr_TR-fahrettin-medium"],
        "fettah": ["tr_TR-fettah-medium"]
    },
    "uk_UA": {
        "lada": ["uk_UA-lada-x_low"],
        "ukrainian_tts": ["uk_UA-ukrainian_tts-medium"]
    },
    "vi_VN": {
        "25hours_single": ["vi_VN-25hours_single-low"],
        "vais1000": ["vi_VN-vais1000-medium"],
        "vivos": ["vi_VN-vivos-x_low"]
    },
    "zh_CN": {
        "huayan": ["zh_CN-huayan-x_low", "zh_CN-huayan-medium"]
    }
}

COUNTRYS = list(PIPER_MODELS.keys())
MODELS = []
for country in COUNTRYS:
    for model in PIPER_MODELS[country].keys():
        MODELS += PIPER_MODELS[country][model]

PIPER_MODEL_DIR = "/opt/piper_models"

class TTS():
    DEFAULT_MODEL = "en_US-danny-low"

    TTS_TEMPELATE = "echo \"{text}\" | piper \
--model {model} \
--output_file {output_file}"

    STREAM_TEMPELATE = "echo \"{text}\" | piper \
--model {model} \
--output-raw | aplay -r 16000 -f S16_LE -t raw -"

    def __init__(self, model=None):
        self.model = None
        if not os.path.exists(PIPER_MODEL_DIR):
            run_command(f"mkdir -p {PIPER_MODEL_DIR}")
            run_command(f"chown 1000:1000 {PIPER_MODEL_DIR}")
        self.set_model(self.DEFAULT_MODEL)

    def set_model(self, model):
        if model in MODELS:
            self.model = model
        else:
            raise ValueError("Model not found")

    def model_downloaded(self, model=None):
        if model is None:
            model = self.model
        onnx_file = os.path.join(PIPER_MODEL_DIR, model + ".onnx")
        json_file = onnx_file + ".json"
        onnx_exists = os.path.exists(onnx_file)
        json_exists = os.path.exists(json_file)
        return onnx_exists and json_exists
    
    def download_model(self, model=None):
        if model is None:
            model = self.model
        print(f"Downloading model: {model}")
        onnx_file = os.path.join(PIPER_MODEL_DIR, model + ".onnx")
        json_file = os.path.join(PIPER_MODEL_DIR, model + ".json")
        run_command(f"piper --model {model} --download-dir {PIPER_MODEL_DIR}")
        run_command(f"chown 1000:1000 {onnx_file}")
        run_command(f"chown 1000:1000 {json_file}")

    def tts(self, text, file):
        if self.model is None:
            raise ValueError("Model not set")
        text = text.replace('"', '\\"')
        model_path = os.path.join(PIPER_MODEL_DIR, self.model + ".onnx")
        args = {
            "text": text,
            "model": model_path,
            "output_file": file
        }
        cmd = self.TTS_TEMPELATE.format(**args)
        status, result = run_command(cmd)
        if status not in [0, None]:
            raise RuntimeError(f"Run command error: \n  Command:{cmd}\n  Status {status}\n  Error: {result}")
        return status == 0

    def stream(self, text):
        if self.model is None:
            raise ValueError("Model not set")
        text = text.replace('"', '\\"')
        model_path = os.path.join(PIPER_MODEL_DIR, self.model + ".onnx")
        args = {
            "text": text,
            "model": model_path
        }
        cmd = self.STREAM_TEMPELATE.format(**args)
        status, result = run_command(cmd)
        if status not in [0, None]:
            raise RuntimeError(f"Run command error: \n  Command:{cmd}\n  Status {status}\n  Error: {result}")

    def say(self, text, stream=True):
        if stream:
            self.stream(text)
        else:
            self.tts(text, "tmp.wav")
            run_command(f"aplay tmp.wav")

    def available_models(self, country=None):
        if country is not None:
            if country not in COUNTRYS:
                raise ValueError("Country not found")
            return PIPER_MODELS[country]
        else:
            return MODELS

    def available_countrys(self):
        return COUNTRYS
