export default function AppHeader(){
    return(
        <header className="mb-10">
            <div className="flex items-center gap-4">
                <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-blue-600 text-2xl text-white shadow-lg">
                      🎓
                </div>
                <div>
                    <h1 className="text-4xl font-bold text-slate-900">ClassLens</h1>
                    <p className="text-slate-600">Helping teachers mark faster</p>
                </div>
            </div>
        </header>
    )
}