-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 30, 2021 at 07:55 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `uas_web`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `admin_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` text NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`admin_id`, `username`, `password`, `first_name`, `last_name`, `email`) VALUES
(1, 'michael', 'admin', 'Melchsee', 'Doa', 'mikedh2612@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `invoices`
--

CREATE TABLE `invoices` (
  `invoice_id` text NOT NULL,
  `user_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `invoices`
--

INSERT INTO `invoices` (`invoice_id`, `user_id`, `product_id`, `quantity`) VALUES
('maikdi_0', 1, 5, 1),
('maikdi_1', 1, 1, 1),
('maikdi_2', 1, 6, 1),
('maikdi_3', 1, 6, 1),
('maikdi_3', 1, 7, 1),
('maikdi_3', 1, 4, 1),
('maikdi_4', 1, 2, 1),
('maikdi_5', 1, 3, 1),
('maikdi_6', 1, 2, 1),
('maikdi_7', 1, 5, 1),
('maikdi_8', 1, 1, 1),
('maikdi_9', 1, 7, 1),
('maikdi_10', 1, 1, 1),
('maikdi_10', 1, 2, 4),
('cthulu_0', 2, 4, 1),
('cthulu_0', 2, 2, 1),
('maikdi_11', 1, 2, 1),
('maikdi_11', 1, 1, 1),
('maikdi_11', 1, 5, 1),
('cthulu_4', 2, 7, 1),
('cthulu_4', 2, 6, 1);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `price` int(11) NOT NULL COMMENT 'Harga dalam Rupiah',
  `kategori` varchar(50) NOT NULL COMMENT 'Kategori benda misalnya: earphone, hp dsb.',
  `Deskripsi` text NOT NULL,
  `path` text NOT NULL COMMENT 'path untuk gambar produk'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `name`, `price`, `kategori`, `Deskripsi`, `path`) VALUES
(1, 'iPhone 13 Pro 128GB 256GB 512GB 1TB Sierra Blue Graphite Gold Silver - INTER 128GB, Silver', 16699000, 'Handphone', 'Iphone 13 Pro<br>Layar : 6.1 inch <br>Memori : 128 GB - 256 GB - 512 GB - 1 TB<br>Warna : Sierra Blue - Graphite - Silver - Gold<br><br>SIMCARD: <br>- IBOX ( Nano + eSim ) <br>- INTER ( Single Nano TANPA esim )<br>- DUAL NANO ( Nano + Nano )<br><br>- Garansi Apple International 1 Tahun<br>- BNIB (Brand New In Box)<br>- Di Dalam box: Unit iPhone + USB-C to Lightning Cable', 'Iphone13.png'),
(2, 'SAMSUNG GALAXY A32 5G - NFC - 8GB 128GB 8/128 GARANSI RESMI - Awesome Black', 3749900, 'Handphone', 'Spesifikasi :<br><br>NETWORK	Technology	<br>GSM / CDMA / HSPA / LTE / 5G<br>LAUNCH	Announced	2021, January 13<br>Status	Available. Released 2021, January 22<br>BODY	Dimensions	164.2 x 76.1 x 9.1 mm (6.46 x 3.00 x 0.36 in)<br>Weight	205 g (7.23 oz)<br>SIM	Single SIM (Nano-SIM) or Hybrid Dual SIM (Nano-SIM, dual stand-by)<br>DISPLAY	Type	TFT<br>Size	6.5 inches, 102.0 cm2 (~81.6% screen-to-body ratio)<br>Resolution	720 x 1600 pixels, 20:9 ratio (~270 ppi density)<br>PLATFORM	OS	Android 11, One UI 3.0<br>Chipset	MediaTek MT6853 Dimensity 720 5G (7 nm)<br>CPU	Octa-core (2x2.0 GHz Cortex-A76 &amp; 6x2.0 GHz Cortex-A55)<br>GPU	Mali-G57 MC3<br>MEMORY	Card slot	microSDXC (uses shared SIM slot)<br>Internal	64GB 4GB RAM, 128GB 4GB RAM, 128GB 6GB RAM, 128GB 8GB RAM<br>MAIN CAMERA	Quad	48 MP, f/1.8, 26mm (wide), 1/2.0\", 0.8µm, PDAF<br>8 MP, f/2.2, 123˚, (ultrawide), 1/4.0\", 1.12µm<br>5 MP, f/2.4, (macro)<br>2 MP, f/2.4, (depth)<br>Features	LED flash, panorama, HDR<br>Video	4K@30fps, 1080p@30/120fps<br>SELFIE CAMERA	Single	13 MP, f/2.2, (wide)<br>Video	1080p@30fps<br>SOUND	Loudspeaker	Yes<br>3.5mm jack	Yes<br>COMMS	WLAN	Wi-Fi 802.11 a/b/g/n/ac, dual-band, Wi-Fi Direct, hotspot<br>Bluetooth	5.0, A2DP, LE<br>GPS	Yes, with A-GPS, GLONASS, GALILEO, BDS<br>NFC	Yes (market/region dependent)<br>Radio	Unspecified<br>USB	USB Type-C 2.0, USB On-The-Go<br>FEATURES	Sensors	Fingerprint (side-mounted), accelerometer, gyro, proximity, compass<br>BATTERY	Type	Li-Ion 5000 mAh, non-removable<br>Charging	Fast charging 15W<br>MISC	Colors	Awesome Black, Awesome White, Awesome Blue, Awesome Violet', 'Samsung-Galaxy-A32-Violet.jpg'),
(3, 'Xiaomi Poco X3 GT 8/128GG + 8/256GB Garansi Resmi - 8/128 Blue', 4199000, 'Handphone', 'NETWORK	Technology	GSM / HSPA / LTE / 5G		<br>LAUNCH	Announced	2021, July 28		<br>Status	Coming soon. Exp. release 2021, August		<br>BODY	Dimensions	163.3 x 75.9 x 8.9 mm (6.43 x 2.99 x 0.35 in)		<br>Weight	193 g (6.81 oz)		<br>Build	Glass front (Gorilla Glass Victus), plastic back		<br>SIM	Dual SIM (Nano-SIM, dual stand-by)		<br> 	IP53, dust and splash protection		<br>DISPLAY	Type	IPS LCD, 120Hz, HDR10, 450 nits (typ)		<br>Size	6.6 inches, 105.2 cm2 (~84.9% screen-to-body ratio)		<br>Resolution	1080 x 2400 pixels, 20:9 ratio (~399 ppi density)		<br>Protection	Corning Gorilla Glass Victus		<br>PLATFORM	OS	Android 11, MIUI 12.5 for POCO		<br>Chipset	MediaTek MT6891Z Dimensity 1100 5G (6 nm)		<br>CPU	Octa-core (4x2.6 GHz Cortex-A78 &amp; 4x2.0 GHz Cortex-A55)		<br>GPU	Mali-G77 MC9		<br>MEMORY	Card slot	No		<br>Internal	128GB 8GB RAM, 256GB 8GB RAM		<br> 	UFS 3.1		<br>MAIN CAMERA	Modules	64 MP, f/1.8, 26mm (wide), 1/1.97\", 0.7µm, PDAF<br>8 MP, f/2.2, 120˚ (ultrawide), 1/4.0\", 1.12µm<br>2 MP, f/2.4, (macro)		<br>Features	LED flash, HDR, panorama		<br>Video	4K@30fps, 1080p@30/60/120fps		<br>SELFIE CAMERA	Modules	16 MP, f/2.5, (wide), 1/3.06\", 1.0µm		<br>Video	1080p@30fps, 720p@120fps, 960fps		<br>SOUND	Loudspeaker	Yes, with stereo speakers		<br>3.5mm jack	No		<br> 	24-bit/192kHz audio<br>Tuned by JBL		<br>COMMS	WLAN	Wi-Fi 802.11 a/b/g/n/ac/6, dual-band, Wi-Fi Direct, hotspot		<br>Bluetooth	5.2, A2DP, LE		<br>GPS	Yes, with A-GPS, GLONASS, GALILEO, BDS, QZSS		<br>NFC	Yes (market/region dependent)		<br>Infrared port	Yes		<br>Radio	No		<br>USB	USB Type-C 2.0		<br>FEATURES	Sensors	Fingerprint (side-mounted), accelerometer, gyro, compass, color spectrum		<br> 	Virtual proximity sensing		<br>BATTERY	Type	Li-Po 5000 mAh, non-removable</div>', 'Xiaomi_poco.jpg'),
(4, 'oppo reno 5 marvel edition 8gb/128gb', 6700000, 'Handphone', 'Spesifikasi:<br><br>Size and Weight : 7.7mm/7.8mm |171g]<br><br>Memory : 8GB/128GB<br><br>Display : 6.4\" AMOLED FHD+ (2400 x 1800), Single Punch Hole 90Hz (hidden fingerpoint 3.0)<br>Rear camera: main lens 64MP + wide angle 8MP + macro 2MP + mono 2MP<br><br>Front camera 44MP<br><br>Processor : Qualcomm 720G (8nm) Octacore 2.3GHz<br><br>Battery : 4310 mAh / High Voltage Fast Charge<br><br>OS : Colos OS 11 on Android 11<br><br>Network : 2G/3G/4G<br><br>NFC : Yes', 'Poco_reno.jpg'),
(5, 'Headphone Samson SR850 / SR 850 / SR-850 Packing Box', 575000, 'Headphone', 'Samson SR850 Studio Monitor Headphones ( Packing Box )<br><br>Samson\'s SR850 Professional Studio Reference Headphones offer an Outstanding listening solution for musicians, sound engineers and general music eanthusiasts alike. With solid bass response , ultra clear highs and an open ear design for a more ambient listening experience , the SR850s ensutr complete comfort and accurate headphone monitoring.<br>&gt;&gt; Open ear design for enhancend ambient listening<br>&gt;&gt; 50mm drivers for exceptional reproduction and wide dynamic range <br>&gt;&gt; 10Hz - 30kHz frequancy response <br>&gt;&gt; 32 impedance <br>&gt;&gt; Self adjusting headband for a secure, comfortable fit<br>&gt;&gt; 1/8 inch to 1/4 inch gold plated adapter included', 'Samson_SR850.jpg'),
(6, 'SONY WI-XB400 Black Extra Bass Wireless Earphone / WI XB400 / WIXB400', 438940, 'Earphone', 'Deep and punchy sound to enhance the everyday<br>As part of Sony’s EXTRA BASS™ range, the<br>WI-XB400 are lightweight but pack a punch. Enhancing low-end frequencies, these headphones deliver exceptional bass, lifting each and every track<br><br>•	Feel the power of extra bass<br>•	Wireless Audio with Bluetooth technology<br>•	Up to 15 hours of battery life with Quick charging (10min charge = 60min of playback)<br>•	12mm driver units for crisp, clear sound<br>•	Flexible and lightweight cables<br>•	Hands-free calling and voice assistant compatible<br>•	Magnetic buds for easy carrying<br>•	In the box: USB Type-C<br><br>All day power and quick charging<br>Enjoy up to 15 hours of non-stop music. If your headphones are running low on power, a 10-minute quick charge will give you up to 60 minutes of play time.<br><br>Easy operation with buttons<br>Use the buttons to play, stop, or skip through tracks and adjust the volume.<br>Voice-assistant compatible<br><br>A simple button press connects you to your smartphone\'s voice assistant to get directions, play music, and communicate with contacts<br><br>Easy hands-free calling<br>Conversation flows freely with easy hands-free calling, thanks to the built-in microphone. No need to even take your phone from your pocket.<br><br>General Features<br>HEADPHONE TYPE: Closed Dynamic<br>DRIVER UNIT: 0.47 \"<br>MAGNET: Neodymium<br>FREQUENCY RESPONSE (BLUETOOTH® COMMUNICATION): 20 Hz–20,000 Hz (44.1 kHz Sampling)<br>VOLUME CONTROL: Yes<br>WEARING STYLE: Neckband style<br><br>Battery<br>BATTERY CHARGE TIME: Approx. 3 hrs (Full charge)<br>BATTERY CHARGE METHOD: USB type-C<br>BATTERY LIFE (CONTINUOUS MUSIC PLAYBACK TIME): Max. 15 h (Full charge)<br>BATTERY LIFE (CONTINUOUS COMMUNICATION TIME): Max. 15 h (Full charge)<br>BATTERY LIFE (WAITING TIME): Max. 200 h (Full charge)<br><br>Bluetooth® Specification<br>BLUETOOTH® VERSION: 5.0<br>EFFECTIVE RANGE: Line of sight approx. 30 ft (10 m)<br>FREQUENCY RANGE: 2.4 GHz band', 'Sony_XB.jpeg'),
(7, 'Moondrop Aria 2021 High Performance LCP Diaphragm In Ear Earphone', 1250000, 'Earphone', 'aminan Produk Original<br>Garansi Resmi 1 Tahun<br><br>Earphone Specification :<br>Driver Unit : LCP liquid crystal diaphragm-10mm diameter double cavity magnetic Diaphragm Dynamic unit<br>Headphone Socket : 0.78pin<br>Sensitivity : 122dB/Vrms (@1kHz)<br>Frequency response : 5Hz-36000Hz<br>Effective frequency response : 20Hz~20000Hz<br>', 'moondrop-aria.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

CREATE TABLE `sales` (
  `sales_id` int(11) NOT NULL,
  `invoice_id` text NOT NULL,
  `amount` int(11) NOT NULL,
  `date` datetime NOT NULL COMMENT 'YYYY-MM-DD HH-MM-SS'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sales`
--

INSERT INTO `sales` (`sales_id`, `invoice_id`, `amount`, `date`) VALUES
(13, 'maikdi_10', 31698600, '2021-12-28 22:27:30'),
(14, 'cthulu_0', 10449900, '2021-12-28 22:30:40'),
(18, 'maikdi_11', 21023900, '2021-12-30 00:59:22'),
(19, 'cthulu_4', 1688940, '2021-12-30 01:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` text NOT NULL,
  `num_sales` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `first_name`, `last_name`, `email`, `num_sales`) VALUES
(1, 'maikdi', '123456', 'Michael', 'David', 'mhanitio64@students.calvin.ac.id', 12),
(2, 'cthulu', 'hahaha', 'Charis', 'Hulu', 'chulu17@students.calvin.ac.id', 5);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`sales_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admins`
--
ALTER TABLE `admins`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `sales`
--
ALTER TABLE `sales`
  MODIFY `sales_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
