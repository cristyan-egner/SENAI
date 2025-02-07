-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 06-Fev-2025 às 19:23
-- Versão do servidor: 10.4.27-MariaDB
-- versão do PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `cristyanegnerestoque`
--
DROP DATABASE IF EXISTS `cristyanegnerestoque`;
CREATE DATABASE IF NOT EXISTS `cristyanegnerestoque` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `cristyanegnerestoque`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `cliente`
--

CREATE TABLE `cliente` (
  `cod_cliente` int(11) NOT NULL COMMENT 'esse campo armazena o código do cliente',
  `nome_cliente` varchar(50) NOT NULL COMMENT 'esse campo armazena o nome do cliente',
  `endereco` varchar(50) NOT NULL COMMENT 'esse campo armazena o endereço do cliente',
  `cidade` varchar(50) NOT NULL COMMENT 'esse campo armazena a cidade do cliente',
  `cep` varchar(10) NOT NULL COMMENT 'esse campo armazena o cep do cliente',
  `uf` char(2) NOT NULL COMMENT 'esse campo armazena a uf do cliente',
  `cnpj` varchar(30) NOT NULL COMMENT 'esse campo armazena o cnpj do cliente',
  `ie` int(10) NOT NULL COMMENT 'esse campo armazena o ie do cliente'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `cliente`
--

INSERT INTO `cliente` (`cod_cliente`, `nome_cliente`, `endereco`, `cidade`, `cep`, `uf`, `cnpj`, `ie`) VALUES
(20, 'Beth', 'Av Climério n. 45', 'São Paulo', '25679300', 'SP', '3248512673268', 9280),
(110, 'Jorge', 'Rua Caiapó 13', 'Curitiba', '30078500', 'PR', '1451276498349', 0),
(130, 'Edmar', 'Rua da Prais s/n', 'Salvador', '30079300', 'BA', '234632842349', 7121),
(157, 'Paulo', 'Tv. Moraes c/3', 'Londrina', '', 'PR', '328482233242', 1923),
(180, 'Livio', 'Av. Beira Mar n.1256', 'Florianópolis', '30077500', 'SC', '1273657123474', 0),
(222, 'Lúcia', 'Rua Itabira 123 loja 09', 'Belo Horizonte', '22124391', 'MG', '2831521393488', 2985),
(234, 'José', 'Quadra 3 bl. 3 sl 1003', 'Brasilia', '22841650', 'DF', '2176357612323', 2931),
(260, 'Susana', 'Rua Lopes Mendes 12', 'Niterói', '30046500', 'RJ', '217635712329', 2530),
(290, 'Renato', 'Rua Meireles n. 123 bl.2 sl.345', 'São Paulo', '30225900', 'SP', '1327657112314', 1820),
(390, 'Sebastião', 'Rua da Igreja n. 10', 'Uberaba', '30438700', 'MG', '321765472133', 9071),
(410, 'Rodolfo', 'Largo da Lapa 27 sobrado', 'Rio de Janeiro', '30078900', 'RJ', '1283512823469', 7431),
(720, 'Ana', 'Rua 17 n. 19', 'Niteroi', '24358310', 'RJ', '12113231/0001-34', 2134),
(830, 'Mauricio', 'Av Paulista 1236 sl/2345', 'São Paulo', '3012683', 'SP', '3281698574656', 9343),
(870, 'Flavio', 'Av. Pres Vargas 10', 'São Paulo', '22763931', 'SP', '2253412693879', 4631);

-- --------------------------------------------------------

--
-- Estrutura da tabela `pedido`
--

CREATE TABLE `pedido` (
  `num_pedido` int(11) NOT NULL,
  `prazo_entrega` int(10) DEFAULT NULL,
  `cod_cliente` int(11) NOT NULL,
  `cod_vendedor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `pedido`
--

INSERT INTO `pedido` (`num_pedido`, `prazo_entrega`, `cod_cliente`, `cod_vendedor`) VALUES
(91, 20, 260, 11),
(97, 20, 720, 101),
(98, 20, 410, 209),
(101, 15, 720, 101),
(103, 20, 260, 11),
(104, 30, 110, 101),
(105, 15, 180, 240),
(108, 15, 290, 310),
(111, 20, 260, 240),
(112, 20, 260, 240),
(119, 30, 390, 250),
(121, 20, 410, 209),
(127, 10, 410, 11),
(137, 20, 720, 720),
(138, 20, 260, 11),
(143, 30, 20, 111),
(148, 20, 720, 101),
(189, 15, 870, 213),
(203, 30, 830, 250);

-- --------------------------------------------------------

--
-- Estrutura da tabela `pedido_has_produto`
--

CREATE TABLE `pedido_has_produto` (
  `pedido_num_pedido` int(11) NOT NULL,
  `produto_cod_produto` int(11) NOT NULL,
  `quantidade` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `pedido_has_produto`
--

INSERT INTO `pedido_has_produto` (`pedido_num_pedido`, `produto_cod_produto`, `quantidade`) VALUES
(91, 77, 40),
(97, 77, 20),
(101, 31, 9),
(103, 53, 37),
(104, 53, 32),
(105, 78, 10),
(108, 13, 17),
(111, 25, 10),
(111, 78, 70),
(119, 13, 6),
(119, 22, 10),
(119, 53, 43),
(119, 77, 40),
(121, 25, 10),
(121, 31, 35),
(137, 13, 8),
(138, 22, 10),
(138, 53, 18),
(138, 77, 35),
(143, 31, 20),
(148, 25, 10),
(148, 31, 7),
(148, 45, 8),
(148, 77, 3),
(148, 78, 30),
(189, 78, 45),
(203, 31, 6);

-- --------------------------------------------------------

--
-- Estrutura da tabela `produto`
--

CREATE TABLE `produto` (
  `cod_produto` int(11) NOT NULL COMMENT 'esse campo armazena o código do produto',
  `unid_produto` varchar(10) NOT NULL COMMENT 'esse campo armazena a unidade do produto',
  `desc_produto` varchar(50) NOT NULL COMMENT 'esse campo armazena a descrição do produto',
  `valor_unit` decimal(15,2) NOT NULL COMMENT 'esse campo armazena o valor unitário do produto'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `produto`
--

INSERT INTO `produto` (`cod_produto`, `unid_produto`, `desc_produto`, `valor_unit`) VALUES
(13, 'G', 'Ouro', '6.18'),
(22, 'M', 'Linho', '0.11'),
(25, 'Kg', 'Queijo', '0.97'),
(30, 'SAC', 'Açucar', '0.30'),
(31, 'Bar', 'Chocolate', '0.87'),
(45, 'M', 'Madeira', '0.25'),
(53, 'M', 'Linha', '1.80'),
(77, 'M', 'Papel', '1.05'),
(78, 'L', 'Vinho', '2.00'),
(87, 'M', 'Cano', '1.97');

-- --------------------------------------------------------

--
-- Estrutura da tabela `vendedor`
--

CREATE TABLE `vendedor` (
  `cod_vendedor` int(11) NOT NULL COMMENT 'esse campo armazena o código do vendedor',
  `nome_vendedor` varchar(50) NOT NULL COMMENT 'esse campo armazena o nome do vendedor',
  `sal_fixo` decimal(15,2) NOT NULL COMMENT 'esse campo armazena o salário fixo do vendedor',
  `faixa_comissao` char(2) NOT NULL COMMENT 'esse campo armazena a faixa de comissao do vendedor'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `vendedor`
--

INSERT INTO `vendedor` (`cod_vendedor`, `nome_vendedor`, `sal_fixo`, `faixa_comissao`) VALUES
(11, 'João', '2780.00', 'C'),
(101, 'João', '2650.32', 'C'),
(111, 'Carlos', '2490.00', 'A'),
(209, 'José', '1800.00', 'C'),
(213, 'Jonas', '2300.50', 'A'),
(240, 'Antonio', '9500.00', 'C'),
(250, 'Mauricío', '2930.00', 'B'),
(310, 'Josias', '870.00', 'B'),
(720, 'Felipe', '4600.00', 'A');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`cod_cliente`);

--
-- Índices para tabela `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`num_pedido`),
  ADD KEY `FK_CLIENTE_PEDIDO` (`cod_cliente`),
  ADD KEY `FK_VENDEDOR_PEDIDO` (`cod_vendedor`);

--
-- Índices para tabela `pedido_has_produto`
--
ALTER TABLE `pedido_has_produto`
  ADD PRIMARY KEY (`pedido_num_pedido`,`produto_cod_produto`),
  ADD KEY `fk_pedido_has_produto_produto1_idx` (`produto_cod_produto`),
  ADD KEY `fk_pedido_has_produto_pedido_idx` (`pedido_num_pedido`);

--
-- Índices para tabela `produto`
--
ALTER TABLE `produto`
  ADD PRIMARY KEY (`cod_produto`);

--
-- Índices para tabela `vendedor`
--
ALTER TABLE `vendedor`
  ADD PRIMARY KEY (`cod_vendedor`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `pedido`
--
ALTER TABLE `pedido`
  ADD CONSTRAINT `FK_CLIENTE_PEDIDO` FOREIGN KEY (`cod_cliente`) REFERENCES `cliente` (`cod_cliente`),
  ADD CONSTRAINT `FK_VENDEDOR_PEDIDO` FOREIGN KEY (`cod_vendedor`) REFERENCES `vendedor` (`cod_vendedor`);

--
-- Limitadores para a tabela `pedido_has_produto`
--
ALTER TABLE `pedido_has_produto`
  ADD CONSTRAINT `fk_pedido_has_produto_pedido` FOREIGN KEY (`pedido_num_pedido`) REFERENCES `pedido` (`num_pedido`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_pedido_has_produto_produto1` FOREIGN KEY (`produto_cod_produto`) REFERENCES `produto` (`cod_produto`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
