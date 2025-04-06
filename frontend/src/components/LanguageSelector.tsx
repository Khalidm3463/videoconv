import React from 'react'

interface Props {
  selected: string
  onChange: (lang: string) => void
}

const LANGUAGES = [
  { code: "en", name: "English" },
  { code: "es", name: "Spanish" },
  { code: "fr", name: "French" },
  { code: "hi", name: "Hindi" },
  { code: "de", name: "German" },
  { code: "zh", name: "Chinese" },
  { code: "ja", name: "Japanese" },
  { code: "ru", name: "Russian" },
  { code: "ar", name: "Arabic" },
  { code: "pt", name: "Portuguese" },
]

const LanguageSelector: React.FC<Props> = ({ selected, onChange }) => {
  return (
    <select
      className="border px-3 py-2 rounded-md"
      value={selected}
      onChange={(e) => onChange(e.target.value)}
    >
      {LANGUAGES.map(lang => (
        <option key={lang.code} value={lang.code}>
          {lang.name}
        </option>
      ))}
    </select>
  )
}

export default LanguageSelector
