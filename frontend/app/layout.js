import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata = {
  title: {
    default:"ClassLens",
    template: "%s | ClassLens",
  },
  description: "Helping teachers mark student work faster.",
  manifest: "/manifest.webmanifest",
  icons:{
    icon:"/icon-192.png",
    apple:"/apple-touch-icon.png"
  }
};

export const viewport = {
  themeColor: "#2563eb",
};



export default function RootLayout({ children }) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col">{children}</body>
    </html>
  );
}
