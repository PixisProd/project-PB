import React from "react"
import { DocumentDuplicateIcon } from "@heroicons/react/24/outline"


type CardProps = {
    title: string
    use_case: string
    model: string
    onCopy: () => void
}


const PromptCard: React.FC<CardProps> = ({title, use_case, model, onCopy}) => {
    return (
        <div className="h-[270px] w-[220px] p-2  bg-pbgray border border-pbborder rounded-2xl hover:border-pbwhite transition">
            <h2 className="text-pbwhite text-base font-semibold">{title}</h2>
        </div>
    )
}

export default PromptCard;