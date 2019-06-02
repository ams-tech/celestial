# Created by Adam at 6/1/2019
Feature: dual_rootfs_update
  Install a new rootfs and configure the system to boot with it using a
  dual-rootfs partition scheme

  Scenario: install rootfs update
    Given a rootfs file formatted with <expected_fs>
    And the sample cmdline file <sample_filename>
    And the rootfs device nodes are <dev1> and <dev2>
    When we update the boot rootfs
    Then the rootfs file is burned into the target device node
